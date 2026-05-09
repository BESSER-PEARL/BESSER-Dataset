





import java.util.List;
import java.util.ArrayList;

public class basecs_LambdaTypeCS extends TemplateableElementCS, TypedRefCS, Nameable {

    private String name;





    private basecs_TypedRefCS basecs_typedrefcs;




    private List<basecs_TypedRefCS> basecs_typedrefcss;




    private basecs_TypedRefCS basecs_typedrefcs;


    public basecs_LambdaTypeCS(
        String name    ) {
        super(
        );
        this.name = name;
        this.basecs_typedrefcss = new ArrayList<>();
    }

    public basecs_LambdaTypeCS(
        String name        ArrayList<basecs_TypedRefCS> basecs_typedrefcss    ) {
        this.name = name;
        this.basecs_typedrefcss = basecs_typedrefcss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public basecs_TypedRefCS getBasecs_typedrefcs() {
        return basecs_typedrefcs;
    }

    public void setBasecs_typedrefcs(basecs_TypedRefCS basecs_typedrefcs) {
        this.basecs_typedrefcs = basecs_typedrefcs;
    }
    public List<basecs_TypedRefCS> getBasecs_typedrefcss() {
        return basecs_typedrefcss;
    }

    public void addBasecs_typedrefcs(Basecs_typedrefcs basecs_typedrefcs) {
        this.basecs_typedrefcss.add(basecs_typedrefcs);
    }
    public basecs_TypedRefCS getBasecs_typedrefcs() {
        return basecs_typedrefcs;
    }

    public void setBasecs_typedrefcs(basecs_TypedRefCS basecs_typedrefcs) {
        this.basecs_typedrefcs = basecs_typedrefcs;
    }

}