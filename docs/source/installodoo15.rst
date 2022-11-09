.. _installodoo:

Installer Odoo 15
=================

Installation des dépendances
----------------------------

.. code-block:: bash

    sudo apt update
    sudo apt upgrade
    sudo apt install python3-dev python3-pip python3-wheel python3-venv
    sudo apt install build-essential libpq-dev libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev


Postgresql
----------
Installation de Postgresql
++++++++++++++++++++++++++

.. code-block:: bash

    sudo apt-get install postgresql

Création du rôle de connexion odoo
++++++++++++++++++++++++++++++++++

Se connecter en tant qu'utilisateur ``postgres``

.. code-block:: bash

    sudo su - postgres

Créer un rôle de connexion ``odoo15``

.. code-block:: bash

    createuser --createdb --no-createrole --superuser --pwprompt odoo15

Vérifier si le rôle de connexion créé est bien un superuser

.. code-block:: py

    psql
    \du
    \q

Se déconnecter de l'utilisateur postgres

.. code-block:: bash

    exit

Création du dossier Odoo
------------------------

.. code-block:: bash

    cd
    mkdir odoo && cd odoo
    mkdir 15.0 && cd 15.0
    mkdir ce

Récupération du code source de Odoo
-----------------------------------

Installer git

.. code-block:: bash

    sudo apt-get install git

Récupérer la branche ``15.0`` de Odoo dans le dossier ~/odoo/15.0/ce

.. code-block:: bash

    cd ~/odoo/15.0/ce
    git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 --single-branch .

Environnement virtuel
---------------------
Création d'un environnement virtuel
+++++++++++++++++++++++++++++++++++

.. code-block:: bash

    cd ~/odoo/15.0
    python3 -m venv ~/odoo/15.0/.env

Installation des modules python
+++++++++++++++++++++++++++++++

.. code-block:: bash

    source ~/odoo/15.0/.env/bin/activate
    pip3 install setuptools wheel
    pip3 install -r ce/requirements.txt

Lancer Odoo
-----------

.. code-block:: bash

    python3 ce/odoo-bin -r odoo15 -w odoo15 --db_host localhost --db_port 5432


Installation de wkhtmltopdf
---------------------------

.. code-block:: bash

    sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
    sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
    sudo apt install -f

