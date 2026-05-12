





import java.util.List;
import java.util.ArrayList;

public class minuml1_ActivityGraph extends StateMachine {






    private List<minuml1_Partition> minuml1_partitions;


    public minuml1_ActivityGraph(
    ) {
        super(
        );
        this.minuml1_partitions = new ArrayList<>();
    }

    public minuml1_ActivityGraph(
        ArrayList<minuml1_Partition> minuml1_partitions    ) {
        this.minuml1_partitions = minuml1_partitions;
    }


    public List<minuml1_Partition> getMinuml1_partitions() {
        return minuml1_partitions;
    }

    public void addMinuml1_partition(Minuml1_partition minuml1_partition) {
        this.minuml1_partitions.add(minuml1_partition);
    }

}