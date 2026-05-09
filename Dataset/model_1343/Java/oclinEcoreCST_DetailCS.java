





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_DetailCS  {

    private String value;
    private String stringName;
    private String idName;





    private oclinEcoreCST_AnnotationCS oclinecorecst_annotationcs;


    public oclinEcoreCST_DetailCS(
        String value,        String stringName,        String idName    ) {
        this.value = value;
        this.stringName = stringName;
        this.idName = idName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getStringname() {
        return stringName;
    }

    public void setStringname(String stringName) {
        this.stringName = stringName;
    }
    public String getIdname() {
        return idName;
    }

    public void setIdname(String idName) {
        this.idName = idName;
    }

    public oclinEcoreCST_AnnotationCS getOclinecorecst_annotationcs() {
        return oclinecorecst_annotationcs;
    }

    public void setOclinecorecst_annotationcs(oclinEcoreCST_AnnotationCS oclinecorecst_annotationcs) {
        this.oclinecorecst_annotationcs = oclinecorecst_annotationcs;
    }

}