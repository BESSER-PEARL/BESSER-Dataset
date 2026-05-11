





import java.util.List;
import java.util.ArrayList;

public class nonemf_MySerializableClass extends Serializable {

    private String somethingInteresting;



    public nonemf_MySerializableClass(
        String somethingInteresting    ) {
        super(
        );
        this.somethingInteresting = somethingInteresting;
    }


    public String getSomethinginteresting() {
        return somethingInteresting;
    }

    public void setSomethinginteresting(String somethingInteresting) {
        this.somethingInteresting = somethingInteresting;
    }


}