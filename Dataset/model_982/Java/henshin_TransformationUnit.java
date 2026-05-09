





import java.util.List;
import java.util.ArrayList;

public class henshin_TransformationUnit extends NamedElement, DescribedElement {

    private boolean activated;





    private List<henshin_Parameter> henshin_parameters;




    private henshin_TransformationSystem henshin_transformationsystem;




    private henshin_Parameter henshin_parameter;


    public henshin_TransformationUnit(
        boolean activated    ) {
        super(
        );
        this.activated = activated;
        this.henshin_parameters = new ArrayList<>();
    }

    public henshin_TransformationUnit(
        boolean activated        ArrayList<henshin_Parameter> henshin_parameters    ) {
        this.activated = activated;
        this.henshin_parameters = henshin_parameters;
    }

    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }

    public List<henshin_Parameter> getHenshin_parameters() {
        return henshin_parameters;
    }

    public void addHenshin_parameter(Henshin_parameter henshin_parameter) {
        this.henshin_parameters.add(henshin_parameter);
    }
    public henshin_TransformationSystem getHenshin_transformationsystem() {
        return henshin_transformationsystem;
    }

    public void setHenshin_transformationsystem(henshin_TransformationSystem henshin_transformationsystem) {
        this.henshin_transformationsystem = henshin_transformationsystem;
    }
    public henshin_Parameter getHenshin_parameter() {
        return henshin_parameter;
    }

    public void setHenshin_parameter(henshin_Parameter henshin_parameter) {
        this.henshin_parameter = henshin_parameter;
    }

}