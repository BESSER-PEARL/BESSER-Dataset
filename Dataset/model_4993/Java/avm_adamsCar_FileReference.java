





import java.util.List;
import java.util.ArrayList;

public class avm_adamsCar_FileReference  {

    private String FilePath;
    private String Name;
    private String ID;





    private List<FileReference> filereferences;




    private List<Parameter> parameters;


    public avm_adamsCar_FileReference(
        String FilePath,        String Name,        String ID    ) {
        this.FilePath = FilePath;
        this.Name = Name;
        this.ID = ID;
        this.filereferences = new ArrayList<>();
        this.parameters = new ArrayList<>();
    }

    public avm_adamsCar_FileReference(
        String FilePath,        String Name,        String ID        ArrayList<FileReference> filereferences,        ArrayList<Parameter> parameters    ) {
        this.FilePath = FilePath;
        this.Name = Name;
        this.ID = ID;
        this.filereferences = filereferences;
        this.parameters = parameters;
    }

    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<FileReference> getFilereferences() {
        return filereferences;
    }

    public void addFilereference(Filereference filereference) {
        this.filereferences.add(filereference);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}