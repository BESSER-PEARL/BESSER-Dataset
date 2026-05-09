





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataModule  {

    private String moduleName;





    private ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule;




    private ddsMetamodel_DdsDataStructure ddsmetamodel_ddsdatastructure;




    private List<ddsMetamodel_DdsDataStructure> ddsmetamodel_ddsdatastructures;




    private ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule;


    public ddsMetamodel_DdsDataModule(
        String moduleName    ) {
        this.moduleName = moduleName;
        this.ddsmetamodel_ddsdatastructures = new ArrayList<>();
    }

    public ddsMetamodel_DdsDataModule(
        String moduleName        ArrayList<ddsMetamodel_DdsDataStructure> ddsmetamodel_ddsdatastructures    ) {
        this.moduleName = moduleName;
        this.ddsmetamodel_ddsdatastructures = ddsmetamodel_ddsdatastructures;
    }

    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }

    public ddsMetamodel_DdsDataModule getDdsmetamodel_ddsdatamodule() {
        return ddsmetamodel_ddsdatamodule;
    }

    public void setDdsmetamodel_ddsdatamodule(ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule) {
        this.ddsmetamodel_ddsdatamodule = ddsmetamodel_ddsdatamodule;
    }
    public ddsMetamodel_DdsDataStructure getDdsmetamodel_ddsdatastructure() {
        return ddsmetamodel_ddsdatastructure;
    }

    public void setDdsmetamodel_ddsdatastructure(ddsMetamodel_DdsDataStructure ddsmetamodel_ddsdatastructure) {
        this.ddsmetamodel_ddsdatastructure = ddsmetamodel_ddsdatastructure;
    }
    public List<ddsMetamodel_DdsDataStructure> getDdsmetamodel_ddsdatastructures() {
        return ddsmetamodel_ddsdatastructures;
    }

    public void addDdsmetamodel_ddsdatastructure(Ddsmetamodel_ddsdatastructure ddsmetamodel_ddsdatastructure) {
        this.ddsmetamodel_ddsdatastructures.add(ddsmetamodel_ddsdatastructure);
    }
    public ddsMetamodel_DdsDataModule getDdsmetamodel_ddsdatamodule() {
        return ddsmetamodel_ddsdatamodule;
    }

    public void setDdsmetamodel_ddsdatamodule(ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule) {
        this.ddsmetamodel_ddsdatamodule = ddsmetamodel_ddsdatamodule;
    }

}