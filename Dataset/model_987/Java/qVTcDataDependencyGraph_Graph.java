





import java.util.List;
import java.util.ArrayList;

public class qVTcDataDependencyGraph_Graph  {

    private String name;





    private List<qVTcDataDependencyGraph_Element> qvtcdatadependencygraph_elements;




    private qVTcDataDependencyGraph_Element qvtcdatadependencygraph_element;


    public qVTcDataDependencyGraph_Graph(
        String name    ) {
        this.name = name;
        this.qvtcdatadependencygraph_elements = new ArrayList<>();
    }

    public qVTcDataDependencyGraph_Graph(
        String name        ArrayList<qVTcDataDependencyGraph_Element> qvtcdatadependencygraph_elements    ) {
        this.name = name;
        this.qvtcdatadependencygraph_elements = qvtcdatadependencygraph_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<qVTcDataDependencyGraph_Element> getQvtcdatadependencygraph_elements() {
        return qvtcdatadependencygraph_elements;
    }

    public void addQvtcdatadependencygraph_element(Qvtcdatadependencygraph_element qvtcdatadependencygraph_element) {
        this.qvtcdatadependencygraph_elements.add(qvtcdatadependencygraph_element);
    }
    public qVTcDataDependencyGraph_Element getQvtcdatadependencygraph_element() {
        return qvtcdatadependencygraph_element;
    }

    public void setQvtcdatadependencygraph_element(qVTcDataDependencyGraph_Element qvtcdatadependencygraph_element) {
        this.qvtcdatadependencygraph_element = qvtcdatadependencygraph_element;
    }

}