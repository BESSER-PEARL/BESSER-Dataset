





import java.util.List;
import java.util.ArrayList;

public class HAL_Entry  {






    private List<TamponType> tampontypes;


    public HAL_Entry(
    ) {
        this.tampontypes = new ArrayList<>();
    }

    public HAL_Entry(
        ArrayList<TamponType> tampontypes    ) {
        this.tampontypes = tampontypes;
    }


    public List<TamponType> getTampontypes() {
        return tampontypes;
    }

    public void addTampontype(Tampontype tampontype) {
        this.tampontypes.add(tampontype);
    }

}