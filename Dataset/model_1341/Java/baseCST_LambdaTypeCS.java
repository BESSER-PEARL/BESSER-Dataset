





import java.util.List;
import java.util.ArrayList;

public class baseCST_LambdaTypeCS extends TypedRefCS, Nameable, TemplateableElementCS {

    private String name;





    private List<baseCST_TypedRefCS> basecst_typedrefcss;




    private baseCST_TypedRefCS basecst_typedrefcs;




    private baseCST_TypedRefCS basecst_typedrefcs;


    public baseCST_LambdaTypeCS(
        String name    ) {
        super(
        );
        this.name = name;
        this.basecst_typedrefcss = new ArrayList<>();
    }

    public baseCST_LambdaTypeCS(
        String name        ArrayList<baseCST_TypedRefCS> basecst_typedrefcss    ) {
        this.name = name;
        this.basecst_typedrefcss = basecst_typedrefcss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<baseCST_TypedRefCS> getBasecst_typedrefcss() {
        return basecst_typedrefcss;
    }

    public void addBasecst_typedrefcs(Basecst_typedrefcs basecst_typedrefcs) {
        this.basecst_typedrefcss.add(basecst_typedrefcs);
    }
    public baseCST_TypedRefCS getBasecst_typedrefcs() {
        return basecst_typedrefcs;
    }

    public void setBasecst_typedrefcs(baseCST_TypedRefCS basecst_typedrefcs) {
        this.basecst_typedrefcs = basecst_typedrefcs;
    }
    public baseCST_TypedRefCS getBasecst_typedrefcs() {
        return basecst_typedrefcs;
    }

    public void setBasecst_typedrefcs(baseCST_TypedRefCS basecst_typedrefcs) {
        this.basecst_typedrefcs = basecst_typedrefcs;
    }

}