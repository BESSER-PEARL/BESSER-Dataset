





import java.util.List;
import java.util.ArrayList;

public class common_DoubleValueMatrix  {






    private List<common_DoubleValueList> common_doublevaluelists;


    public common_DoubleValueMatrix(
    ) {
        this.common_doublevaluelists = new ArrayList<>();
    }

    public common_DoubleValueMatrix(
        ArrayList<common_DoubleValueList> common_doublevaluelists    ) {
        this.common_doublevaluelists = common_doublevaluelists;
    }


    public List<common_DoubleValueList> getCommon_doublevaluelists() {
        return common_doublevaluelists;
    }

    public void addCommon_doublevaluelist(Common_doublevaluelist common_doublevaluelist) {
        this.common_doublevaluelists.add(common_doublevaluelist);
    }

}