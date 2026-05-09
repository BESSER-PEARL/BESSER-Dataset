





import java.util.List;
import java.util.ArrayList;

public class express_core_Instance  {






    private List<DataType> datatypes;




    private List<Population> populations;


    public express_core_Instance(
    ) {
        this.datatypes = new ArrayList<>();
        this.populations = new ArrayList<>();
    }

    public express_core_Instance(
        ArrayList<DataType> datatypes,        ArrayList<Population> populations    ) {
        this.datatypes = datatypes;
        this.populations = populations;
    }


    public List<DataType> getDatatypes() {
        return datatypes;
    }

    public void addDatatype(Datatype datatype) {
        this.datatypes.add(datatype);
    }
    public List<Population> getPopulations() {
        return populations;
    }

    public void addPopulation(Population population) {
        this.populations.add(population);
    }

}