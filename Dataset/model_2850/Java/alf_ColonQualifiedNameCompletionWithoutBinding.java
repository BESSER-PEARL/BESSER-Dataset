





import java.util.List;
import java.util.ArrayList;

public class alf_ColonQualifiedNameCompletionWithoutBinding  {






    private alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding;




    private List<alf_Name> alf_names;


    public alf_ColonQualifiedNameCompletionWithoutBinding(
    ) {
        this.alf_names = new ArrayList<>();
    }

    public alf_ColonQualifiedNameCompletionWithoutBinding(
        ArrayList<alf_Name> alf_names    ) {
        this.alf_names = alf_names;
    }


    public alf_QualifiedNameWithoutBinding getAlf_qualifiednamewithoutbinding() {
        return alf_qualifiednamewithoutbinding;
    }

    public void setAlf_qualifiednamewithoutbinding(alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding) {
        this.alf_qualifiednamewithoutbinding = alf_qualifiednamewithoutbinding;
    }
    public List<alf_Name> getAlf_names() {
        return alf_names;
    }

    public void addAlf_name(Alf_name alf_name) {
        this.alf_names.add(alf_name);
    }

}