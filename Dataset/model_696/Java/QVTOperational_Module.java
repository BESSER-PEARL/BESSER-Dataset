





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_Module extends Package, Class {

    private String isBlackbox;





    private List<ModuleImport> moduleimports;




    private EntryOperation entryoperation;




    private List<Property> propertys;


    public QVTOperational_Module(
        String isBlackbox    ) {
        super(
        );
        this.isBlackbox = isBlackbox;
        this.moduleimports = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public QVTOperational_Module(
        String isBlackbox        ArrayList<ModuleImport> moduleimports,        ArrayList<Property> propertys    ) {
        this.isBlackbox = isBlackbox;
        this.moduleimports = moduleimports;
        this.propertys = propertys;
    }

    public String getIsblackbox() {
        return isBlackbox;
    }

    public void setIsblackbox(String isBlackbox) {
        this.isBlackbox = isBlackbox;
    }

    public List<ModuleImport> getModuleimports() {
        return moduleimports;
    }

    public void addModuleimport(Moduleimport moduleimport) {
        this.moduleimports.add(moduleimport);
    }
    public EntryOperation getEntryoperation() {
        return entryoperation;
    }

    public void setEntryoperation(EntryOperation entryoperation) {
        this.entryoperation = entryoperation;
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}