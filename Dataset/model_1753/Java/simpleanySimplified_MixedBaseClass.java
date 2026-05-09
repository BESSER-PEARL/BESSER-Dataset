





import java.util.List;
import java.util.ArrayList;

public class simpleanySimplified_MixedBaseClass  {






    private List<simpleanySimplified_MixedData> simpleanysimplified_mixeddatas;


    public simpleanySimplified_MixedBaseClass(
    ) {
        this.simpleanysimplified_mixeddatas = new ArrayList<>();
    }

    public simpleanySimplified_MixedBaseClass(
        ArrayList<simpleanySimplified_MixedData> simpleanysimplified_mixeddatas    ) {
        this.simpleanysimplified_mixeddatas = simpleanysimplified_mixeddatas;
    }


    public List<simpleanySimplified_MixedData> getSimpleanysimplified_mixeddatas() {
        return simpleanysimplified_mixeddatas;
    }

    public void addSimpleanysimplified_mixeddata(Simpleanysimplified_mixeddata simpleanysimplified_mixeddata) {
        this.simpleanysimplified_mixeddatas.add(simpleanysimplified_mixeddata);
    }

}