





import java.util.List;
import java.util.ArrayList;

public class Classes_Staff_StaffManager extends IStaff {






    private IStatisticsGenerator istatisticsgenerator;


    public Classes_Staff_StaffManager(
    ) {
        super(
        );
    }



    public IStatisticsGenerator getIstatisticsgenerator() {
        return istatisticsgenerator;
    }

    public void setIstatisticsgenerator(IStatisticsGenerator istatisticsgenerator) {
        this.istatisticsgenerator = istatisticsgenerator;
    }

}