





import java.util.List;
import java.util.ArrayList;

public class Classes_Statistics_StatisticsGenerator extends IStatisticsGenerator {

    private float staticExpenses;





    private IBills ibills;




    private IBookings ibookings;


    public Classes_Statistics_StatisticsGenerator(
        float staticExpenses    ) {
        super(
        );
        this.staticExpenses = staticExpenses;
    }


    public float getStaticexpenses() {
        return staticExpenses;
    }

    public void setStaticexpenses(float staticExpenses) {
        this.staticExpenses = staticExpenses;
    }

    public IBills getIbills() {
        return ibills;
    }

    public void setIbills(IBills ibills) {
        this.ibills = ibills;
    }
    public IBookings getIbookings() {
        return ibookings;
    }

    public void setIbookings(IBookings ibookings) {
        this.ibookings = ibookings;
    }

}