





import java.util.List;
import java.util.ArrayList;

public class alf_UnqualifiedName  {

    private String name;





    private alf_QualifiedNamePath alf_qualifiednamepath;


    public alf_UnqualifiedName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public alf_QualifiedNamePath getAlf_qualifiednamepath() {
        return alf_qualifiednamepath;
    }

    public void setAlf_qualifiednamepath(alf_QualifiedNamePath alf_qualifiednamepath) {
        this.alf_qualifiednamepath = alf_qualifiednamepath;
    }

}