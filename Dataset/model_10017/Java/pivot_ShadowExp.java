





import java.util.List;
import java.util.ArrayList;

public class pivot_ShadowExp extends OCLExpression {

    private String value;





    private List<pivot_ShadowPart> pivot_shadowparts;


    public pivot_ShadowExp(
        String value    ) {
        super(
        );
        this.value = value;
        this.pivot_shadowparts = new ArrayList<>();
    }

    public pivot_ShadowExp(
        String value        ArrayList<pivot_ShadowPart> pivot_shadowparts    ) {
        this.value = value;
        this.pivot_shadowparts = pivot_shadowparts;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<pivot_ShadowPart> getPivot_shadowparts() {
        return pivot_shadowparts;
    }

    public void addPivot_shadowpart(Pivot_shadowpart pivot_shadowpart) {
        this.pivot_shadowparts.add(pivot_shadowpart);
    }

}