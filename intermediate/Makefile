ALL: \
	./source/assess.pqt \
	./source/lut.pqt \
	./source/misc.pqt \
	./source/tax.pqt \
	./intermediate/with_small_apts.pqt

../data/L3_SHP_M176_Medford: ../data
	curl "https://s3.us-east-1.amazonaws.com/download.massgis.digital.mass.gov/shapefiles/l3parcels/L3_SHP_M176_MEDFORD.zip" -o ../data/L3_SHP_M176_MEDFORD.zip
	test -f ../data/L3_SHP_M176_MEDFORD.zip
	unzip ../data/L3_SHP_M176_MEDFORD.zip -d ../data
	rm ../data/L3_SHP_M176_MEDFORD.zip

../data/L3_SHP_M176_Medford/%: ../data/L3_SHP_M176_Medford
	test -f $@

source:
	mkdir -p source

./source/assess-naive.pqt: source ../data/L3_SHP_M176_Medford/M176Assess_CY23_FY23.cpg ../data/L3_SHP_M176_Medford/M176Assess_CY23_FY23.dbf ../data/L3_SHP_M176_Medford/M176Assess_CY23_FY23.dbf.xml
	../bin/2pqt ../data/L3_SHP_M176_Medford/M176Assess_CY23_FY23.dbf ./source/assess-naive.pqt

./source/assess.pqt: source ./source/assess-naive.pqt
	../bin/fixzero SITE_ADDR OWN_ADDR ./source/assess-naive.pqt ./source/assess.pqt

./source/lut.pqt: source ../data/L3_SHP_M176_Medford/M176Assess_CY23_FY23.cpg ../data/L3_SHP_M176_Medford/M176_LUT_CY23_FY23.dbf ../data/L3_SHP_M176_Medford/M176_LUT_CY23_FY23.dbf.xml
	../bin/2pqt ../data/L3_SHP_M176_Medford/M176_LUT_CY23_FY23.dbf ./source/lut.pqt

./source/misc.pqt: source ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.cpg ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.dbf ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.prj ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.sbn ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.sbx ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.shp ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.shp.xml ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.shx
	../bin/2pqt ../data/L3_SHP_M176_Medford/M176Misc_CY23_FY23.shp ./source/misc.pqt

./source/tax.pqt: source ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.cpg ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.dbf ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.prj ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.sbn ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.sbx ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.shp ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.shp.xml ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.shx
	../bin/2pqt ../data/L3_SHP_M176_Medford/M176TaxPar_CY23_FY23.shp ./source/tax.pqt

intermediate:
	mkdir -p intermediate

./intermediate/with_small_apts.pqt: source ../bin/identify_small_apts ./source/assess.pqt intermediate
	../bin/identify_small_apts ./source/assess.pqt ./intermediate/with_small_apts.pqt
