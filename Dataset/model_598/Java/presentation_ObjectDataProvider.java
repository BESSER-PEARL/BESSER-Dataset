





import java.util.List;
import java.util.ArrayList;

public class presentation_ObjectDataProvider extends AbstractDataProvider {

    private String methodName;
    private String group1;





    private List<presentation_Class> presentation_classs;




    private List<presentation_List> presentation_lists;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_ObjectDataProvider(
        String methodName,        String group1    ) {
        super(
        );
        this.methodName = methodName;
        this.group1 = group1;
        this.presentation_classs = new ArrayList<>();
        this.presentation_lists = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_ObjectDataProvider(
        String methodName,        String group1        ArrayList<presentation_Class> presentation_classs,        ArrayList<presentation_List> presentation_lists,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.methodName = methodName;
        this.group1 = group1;
        this.presentation_classs = presentation_classs;
        this.presentation_lists = presentation_lists;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_Class> getPresentation_classs() {
        return presentation_classs;
    }

    public void addPresentation_class(Presentation_class presentation_class) {
        this.presentation_classs.add(presentation_class);
    }
    public List<presentation_List> getPresentation_lists() {
        return presentation_lists;
    }

    public void addPresentation_list(Presentation_list presentation_list) {
        this.presentation_lists.add(presentation_list);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}