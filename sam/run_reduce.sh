#!/bin/sh

pdbname=$1

$AMBERHOME/bin/reduce $pdbname.pdb > ${pdbname}_addH.pdb 
