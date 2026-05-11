





import java.util.List;
import java.util.ArrayList;

public class dag_Vertex  {

    private String id;





    private dag_DAG dag_dag;


    public dag_Vertex(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dag_DAG getDag_dag() {
        return dag_dag;
    }

    public void setDag_dag(dag_DAG dag_dag) {
        this.dag_dag = dag_dag;
    }

}