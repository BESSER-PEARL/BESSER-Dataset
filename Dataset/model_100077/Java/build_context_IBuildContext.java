





import java.util.List;
import java.util.ArrayList;

public class build_context_IBuildContext  {






    private List<IAdvise> iadvises;


    public build_context_IBuildContext(
    ) {
        this.iadvises = new ArrayList<>();
    }

    public build_context_IBuildContext(
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