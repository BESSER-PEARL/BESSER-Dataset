





import java.util.List;
import java.util.ArrayList;

public class Data_Type  {

    private String fullName;
    private String name;
    private boolean isCollection;
    private boolean doesReferenceModelClass;





    private Data_Attribute data_attribute;


    public Data_Type(
        String fullName,        String name,        boolean isCollection,        boolean doesReferenceModelClass    ) {
        this.fullName = fullName;
        this.name = name;
        this.isCollection = isCollection;
        this.doesReferenceModelClass = doesReferenceModelClass;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }
    public boolean getDoesreferencemodelclass() {
        return doesReferenceModelClass;
    }

    public void setDoesreferencemodelclass(boolean doesReferenceModelClass) {
        this.doesReferenceModelClass = doesReferenceModelClass;
    }

    public Data_Attribute getData_attribute() {
        return data_attribute;
    }

    public void setData_attribute(Data_Attribute data_attribute) {
        this.data_attribute = data_attribute;
    }

}