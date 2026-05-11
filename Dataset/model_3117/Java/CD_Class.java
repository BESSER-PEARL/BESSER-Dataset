





import java.util.List;
import java.util.ArrayList;

public class CD_Class extends Classifier {

    private String isAbstract;





    private CD_Class cd_class;




    private List<CD_Attribute> cd_attributes;




    private CD_Attribute cd_attribute;


    public CD_Class(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.cd_attributes = new ArrayList<>();
    }

    public CD_Class(
        String isAbstract        ArrayList<CD_Attribute> cd_attributes    ) {
        this.isAbstract = isAbstract;
        this.cd_attributes = cd_attributes;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public CD_Class getCd_class() {
        return cd_class;
    }

    public void setCd_class(CD_Class cd_class) {
        this.cd_class = cd_class;
    }
    public List<CD_Attribute> getCd_attributes() {
        return cd_attributes;
    }

    public void addCd_attribute(Cd_attribute cd_attribute) {
        this.cd_attributes.add(cd_attribute);
    }
    public CD_Attribute getCd_attribute() {
        return cd_attribute;
    }

    public void setCd_attribute(CD_Attribute cd_attribute) {
        this.cd_attribute = cd_attribute;
    }

}