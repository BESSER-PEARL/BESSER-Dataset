





import java.util.List;
import java.util.ArrayList;

public class micro_ViewService extends Service {






    private List<micro_AggregateService> micro_aggregateservices;


    public micro_ViewService(
    ) {
        super(
        );
        this.micro_aggregateservices = new ArrayList<>();
    }

    public micro_ViewService(
        ArrayList<micro_AggregateService> micro_aggregateservices    ) {
        this.micro_aggregateservices = micro_aggregateservices;
    }


    public List<micro_AggregateService> getMicro_aggregateservices() {
        return micro_aggregateservices;
    }

    public void addMicro_aggregateservice(Micro_aggregateservice micro_aggregateservice) {
        this.micro_aggregateservices.add(micro_aggregateservice);
    }

}