





import java.util.List;
import java.util.ArrayList;

public class references_SelfReference extends Reference {






    private Self self;


    public references_SelfReference(
    ) {
        super(
        );
    }



    public Self getSelf() {
        return self;
    }

    public void setSelf(Self self) {
        this.self = self;
    }

}