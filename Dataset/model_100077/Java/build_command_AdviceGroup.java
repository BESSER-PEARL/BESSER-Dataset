





import java.util.List;
import java.util.ArrayList;

public class build_command_AdviceGroup  {






    private List<IAdvise> iadvises;


    public build_command_AdviceGroup(
    ) {
        this.iadvises = new ArrayList<>();
    }

    public build_command_AdviceGroup(
        ArrayList<IAdvise> iadvises    ) {
        this.iadvises = iadvises;
    }


    public List<IAdvise> getIadvises() {
        return iadvises;
    }

    public void addIadvise(Iadvise iadvise) {
        this.iadvises.add(iadvise);
    }

}