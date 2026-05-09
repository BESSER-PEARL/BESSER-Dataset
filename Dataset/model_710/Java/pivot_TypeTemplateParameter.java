





import java.util.List;
import java.util.ArrayList;

public class pivot_TypeTemplateParameter extends TemplateParameter {

    private String allowSubstitutable;





    private List<pivot_Type> pivot_types;


    public pivot_TypeTemplateParameter(
        String allowSubstitutable    ) {
        super(
        );
        this.allowSubstitutable = allowSubstitutable;
        this.pivot_types = new ArrayList<>();
    }

    public pivot_TypeTemplateParameter(
        String allowSubstitutable        ArrayList<pivot_Type> pivot_types    ) {
        this.allowSubstitutable = allowSubstitutable;
        this.pivot_types = pivot_types;
    }

    public String getAllowsubstitutable() {
        return allowSubstitutable;
    }

    public void setAllowsubstitutable(String allowSubstitutable) {
        this.allowSubstitutable = allowSubstitutable;
    }

    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }

}