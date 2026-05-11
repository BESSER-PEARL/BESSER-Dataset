





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Operation extends Feature {

    private String visibility;





    private List<domainmodel_Parameter> domainmodel_parameters;


    public domainmodel_Operation(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
        this.domainmodel_parameters = new ArrayList<>();
    }

    public domainmodel_Operation(
        String visibility        ArrayList<domainmodel_Parameter> domainmodel_parameters    ) {
        this.visibility = visibility;
        this.domainmodel_parameters = domainmodel_parameters;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public List<domainmodel_Parameter> getDomainmodel_parameters() {
        return domainmodel_parameters;
    }

    public void addDomainmodel_parameter(Domainmodel_parameter domainmodel_parameter) {
        this.domainmodel_parameters.add(domainmodel_parameter);
    }

}