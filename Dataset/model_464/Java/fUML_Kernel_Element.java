





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Element  {






    private List<Kernel_Comment> kernel_comments;




    private List<Kernel_Element> kernel_elements;




    private Kernel_Element kernel_element;


    public fUML_Kernel_Element(
    ) {
        this.kernel_comments = new ArrayList<>();
        this.kernel_elements = new ArrayList<>();
    }

    public fUML_Kernel_Element(
        ArrayList<Kernel_Comment> kernel_comments,        ArrayList<Kernel_Element> kernel_elements    ) {
        this.kernel_comments = kernel_comments;
        this.kernel_elements = kernel_elements;
    }


    public List<Kernel_Comment> getKernel_comments() {
        return kernel_comments;
    }

    public void addKernel_comment(Kernel_comment kernel_comment) {
        this.kernel_comments.add(kernel_comment);
    }
    public List<Kernel_Element> getKernel_elements() {
        return kernel_elements;
    }

    public void addKernel_element(Kernel_element kernel_element) {
        this.kernel_elements.add(kernel_element);
    }
    public Kernel_Element getKernel_element() {
        return kernel_element;
    }

    public void setKernel_element(Kernel_Element kernel_element) {
        this.kernel_element = kernel_element;
    }

}