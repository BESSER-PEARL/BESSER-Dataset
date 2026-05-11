





import java.util.List;
import java.util.ArrayList;

public class alf_PositionalTemplateBinding extends TemplateBinding {






    private List<alf_QualifiedName> alf_qualifiednames;


    public alf_PositionalTemplateBinding(
    ) {
        super(
        );
        this.alf_qualifiednames = new ArrayList<>();
    }

    public alf_PositionalTemplateBinding(
        ArrayList<alf_QualifiedName> alf_qualifiednames    ) {
        this.alf_qualifiednames = alf_qualifiednames;
    }


    public List<alf_QualifiedName> getAlf_qualifiednames() {
        return alf_qualifiednames;
    }

    public void addAlf_qualifiedname(Alf_qualifiedname alf_qualifiedname) {
        this.alf_qualifiednames.add(alf_qualifiedname);
    }

}