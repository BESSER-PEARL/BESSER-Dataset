





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Case_List  {






    private List<Case_List_Element> case_list_elements;


    public iec61131_st_Case_List(
    ) {
        this.case_list_elements = new ArrayList<>();
    }

    public iec61131_st_Case_List(
        ArrayList<Case_List_Element> case_list_elements    ) {
        this.case_list_elements = case_list_elements;
    }


    public List<Case_List_Element> getCase_list_elements() {
        return case_list_elements;
    }

    public void addCase_list_element(Case_list_element case_list_element) {
        this.case_list_elements.add(case_list_element);
    }

}