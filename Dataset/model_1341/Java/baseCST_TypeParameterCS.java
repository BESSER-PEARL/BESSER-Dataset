





import java.util.List;
import java.util.ArrayList;

public class baseCST_TypeParameterCS extends TypeCS, TemplateParameterCS {






    private baseCST_TypedRefCS basecst_typedrefcs;




    private List<baseCST_TypedRefCS> basecst_typedrefcss;


    public baseCST_TypeParameterCS(
    ) {
        super(
        );
        this.basecst_typedrefcss = new ArrayList<>();
    }

    public baseCST_TypeParameterCS(
        ArrayList<baseCST_TypedRefCS> basecst_typedrefcss    ) {
        this.basecst_typedrefcss = basecst_typedrefcss;
    }


    public baseCST_TypedRefCS getBasecst_typedrefcs() {
        return basecst_typedrefcs;
    }

    public void setBasecst_typedrefcs(baseCST_TypedRefCS basecst_typedrefcs) {
        this.basecst_typedrefcs = basecst_typedrefcs;
    }
    public List<baseCST_TypedRefCS> getBasecst_typedrefcss() {
        return basecst_typedrefcss;
    }

    public void addBasecst_typedrefcs(Basecst_typedrefcs basecst_typedrefcs) {
        this.basecst_typedrefcss.add(basecst_typedrefcs);
    }

}