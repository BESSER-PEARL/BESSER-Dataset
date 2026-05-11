





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Modifier extends Feature {

    private boolean many;
    private String name;
    private boolean static;
    private String visibility;
    private String final;





    private domainmodel_Type domainmodel_type;


    public domainmodel_Modifier(
        boolean many,        String name,        boolean static,        String visibility,        String final    ) {
        super(
        );
        this.many = many;
        this.name = name;
        this.static = static;
        this.visibility = visibility;
        this.final = final;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }

}