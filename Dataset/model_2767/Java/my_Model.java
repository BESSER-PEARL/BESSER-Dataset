





import java.util.List;
import java.util.ArrayList;

public class my_Model  {






    private List<my_BType> my_btypes;


    public my_Model(
    ) {
        this.my_btypes = new ArrayList<>();
    }

    public my_Model(
        ArrayList<my_BType> my_btypes    ) {
        this.my_btypes = my_btypes;
    }


    public List<my_BType> getMy_btypes() {
        return my_btypes;
    }

    public void addMy_btype(My_btype my_btype) {
        this.my_btypes.add(my_btype);
    }

}