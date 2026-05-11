





import java.util.List;
import java.util.ArrayList;

public class lobj_Course extends LearningObject {

    private String outlineAsXml;





    private lobj_Category lobj_category;




    private lobj_CourseMeta lobj_coursemeta;




    private List<lobj_Module> lobj_modules;


    public lobj_Course(
        String outlineAsXml    ) {
        super(
        );
        this.outlineAsXml = outlineAsXml;
        this.lobj_modules = new ArrayList<>();
    }

    public lobj_Course(
        String outlineAsXml        ArrayList<lobj_Module> lobj_modules    ) {
        this.outlineAsXml = outlineAsXml;
        this.lobj_modules = lobj_modules;
    }

    public String getOutlineasxml() {
        return outlineAsXml;
    }

    public void setOutlineasxml(String outlineAsXml) {
        this.outlineAsXml = outlineAsXml;
    }

    public lobj_Category getLobj_category() {
        return lobj_category;
    }

    public void setLobj_category(lobj_Category lobj_category) {
        this.lobj_category = lobj_category;
    }
    public lobj_CourseMeta getLobj_coursemeta() {
        return lobj_coursemeta;
    }

    public void setLobj_coursemeta(lobj_CourseMeta lobj_coursemeta) {
        this.lobj_coursemeta = lobj_coursemeta;
    }
    public List<lobj_Module> getLobj_modules() {
        return lobj_modules;
    }

    public void addLobj_module(Lobj_module lobj_module) {
        this.lobj_modules.add(lobj_module);
    }

}