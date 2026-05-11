





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPExternalHeaderInclusion  {

    private String comment;





    private cppmodel_CPPSourceFile cppmodel_cppsourcefile;


    public cppmodel_CPPExternalHeaderInclusion(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cppmodel_CPPSourceFile getCppmodel_cppsourcefile() {
        return cppmodel_cppsourcefile;
    }

    public void setCppmodel_cppsourcefile(cppmodel_CPPSourceFile cppmodel_cppsourcefile) {
        this.cppmodel_cppsourcefile = cppmodel_cppsourcefile;
    }

}