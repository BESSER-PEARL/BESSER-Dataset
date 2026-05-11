





import java.util.List;
import java.util.ArrayList;

public class alf_ColonQualifiedNameCompletionOfImportReference extends ImportReferenceQualifiedNameCompletion {

    private boolean star;





    private alf_AliasDefinition alf_aliasdefinition;




    private List<alf_Name> alf_names;


    public alf_ColonQualifiedNameCompletionOfImportReference(
        boolean star    ) {
        super(
        );
        this.star = star;
        this.alf_names = new ArrayList<>();
    }

    public alf_ColonQualifiedNameCompletionOfImportReference(
        boolean star        ArrayList<alf_Name> alf_names    ) {
        this.star = star;
        this.alf_names = alf_names;
    }

    public boolean getStar() {
        return star;
    }

    public void setStar(boolean star) {
        this.star = star;
    }

    public alf_AliasDefinition getAlf_aliasdefinition() {
        return alf_aliasdefinition;
    }

    public void setAlf_aliasdefinition(alf_AliasDefinition alf_aliasdefinition) {
        this.alf_aliasdefinition = alf_aliasdefinition;
    }
    public List<alf_Name> getAlf_names() {
        return alf_names;
    }

    public void addAlf_name(Alf_name alf_name) {
        this.alf_names.add(alf_name);
    }

}