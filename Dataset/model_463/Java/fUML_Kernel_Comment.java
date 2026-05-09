





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Comment  {

    private String body;





    private List<Kernel_Element> kernel_elements;


    public fUML_Kernel_Comment(
        String body    ) {
        this.body = body;
        this.kernel_elements = new ArrayList<>();
    }

    public fUML_Kernel_Comment(
        String body        ArrayList<Kernel_Element> kernel_elements    ) {
        this.body = body;
        this.kernel_elements = kernel_elements;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<Kernel_Element> getKernel_elements() {
        return kernel_elements;
    }

    public void addKernel_element(Kernel_element kernel_element) {
        this.kernel_elements.add(kernel_element);
    }

}