





import java.util.List;
import java.util.ArrayList;

public class alf_NameList  {






    private List<alf_Name> alf_names;




    private alf_Annotation alf_annotation;


    public alf_NameList(
    ) {
        this.alf_names = new ArrayList<>();
    }

    public alf_NameList(
        ArrayList<alf_Name> alf_names    ) {
        this.alf_names = alf_names;
    }


    public List<alf_Name> getAlf_names() {
        return alf_names;
    }

    public void addAlf_name(Alf_name alf_name) {
        this.alf_names.add(alf_name);
    }
    public alf_Annotation getAlf_annotation() {
        return alf_annotation;
    }

    public void setAlf_annotation(alf_Annotation alf_annotation) {
        this.alf_annotation = alf_annotation;
    }

}