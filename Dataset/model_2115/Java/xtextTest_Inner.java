





import java.util.List;
import java.util.ArrayList;

public class xtextTest_Inner  {

    private boolean isNull;
    private String assignAsData;
    private boolean isEmpty;
    private String parameter;
    private String assignAsBool;
    private String value;
    private boolean isNotNull;





    private xtextTest_Element xtexttest_element;




    private List<xtextTest_Element> xtexttest_elements;




    private xtextTest_Element xtexttest_element;


    public xtextTest_Inner(
        boolean isNull,        String assignAsData,        boolean isEmpty,        String parameter,        String assignAsBool,        String value,        boolean isNotNull    ) {
        this.isNull = isNull;
        this.assignAsData = assignAsData;
        this.isEmpty = isEmpty;
        this.parameter = parameter;
        this.assignAsBool = assignAsBool;
        this.value = value;
        this.isNotNull = isNotNull;
        this.xtexttest_elements = new ArrayList<>();
    }

    public xtextTest_Inner(
        boolean isNull,        String assignAsData,        boolean isEmpty,        String parameter,        String assignAsBool,        String value,        boolean isNotNull        ArrayList<xtextTest_Element> xtexttest_elements    ) {
        this.isNull = isNull;
        this.assignAsData = assignAsData;
        this.isEmpty = isEmpty;
        this.parameter = parameter;
        this.assignAsBool = assignAsBool;
        this.value = value;
        this.isNotNull = isNotNull;
        this.xtexttest_elements = xtexttest_elements;
    }

    public boolean getIsnull() {
        return isNull;
    }

    public void setIsnull(boolean isNull) {
        this.isNull = isNull;
    }
    public String getAssignasdata() {
        return assignAsData;
    }

    public void setAssignasdata(String assignAsData) {
        this.assignAsData = assignAsData;
    }
    public boolean getIsempty() {
        return isEmpty;
    }

    public void setIsempty(boolean isEmpty) {
        this.isEmpty = isEmpty;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }
    public String getAssignasbool() {
        return assignAsBool;
    }

    public void setAssignasbool(String assignAsBool) {
        this.assignAsBool = assignAsBool;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
        this.isNotNull = isNotNull;
    }

    public xtextTest_Element getXtexttest_element() {
        return xtexttest_element;
    }

    public void setXtexttest_element(xtextTest_Element xtexttest_element) {
        this.xtexttest_element = xtexttest_element;
    }
    public List<xtextTest_Element> getXtexttest_elements() {
        return xtexttest_elements;
    }

    public void addXtexttest_element(Xtexttest_element xtexttest_element) {
        this.xtexttest_elements.add(xtexttest_element);
    }
    public xtextTest_Element getXtexttest_element() {
        return xtexttest_element;
    }

    public void setXtexttest_element(xtextTest_Element xtexttest_element) {
        this.xtexttest_element = xtexttest_element;
    }

}