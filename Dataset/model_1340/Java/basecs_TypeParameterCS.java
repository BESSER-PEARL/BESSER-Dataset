





import java.util.List;
import java.util.ArrayList;

public class basecs_TypeParameterCS extends TypeCS, TemplateParameterCS {






    private List<basecs_TypedRefCS> basecs_typedrefcss;




    private basecs_TypedRefCS basecs_typedrefcs;


    public basecs_TypeParameterCS(
    ) {
        super(
        );
        this.basecs_typedrefcss = new ArrayList<>();
    }

    public basecs_TypeParameterCS(
        ArrayList<basecs_TypedRefCS> basecs_typedrefcss    ) {
        this.basecs_typedrefcss = basecs_typedrefcss;
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