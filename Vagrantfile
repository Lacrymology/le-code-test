# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # local box
  config.vm.define :local, primary: true do |local|
    local.vm.box_url = "https://vagrantcloud.com/ubuntu/trusty64"
    local.vm.hostname = "local"

    # Django runserver networking
    local.vm.network "forwarded_port", guest: 8888, host: 8888
    local.vm.network "forwarded_port", guest: 80, host: 8989
    local.vm.network "forwarded_port", guest: 4000, host: 4000

    local.vm.provision "shell",
      path:"./scripts/server-setup.sh", args: ["dev", "vagrant"]

    # VirtualBox Provider config
    local.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
    end
  end

end
