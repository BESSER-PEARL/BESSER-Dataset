





import java.util.List;
import java.util.ArrayList;

public class generics_CallTypeArgumentable extends Commentable {






    private List<TypeArgument> typearguments;


    public generics_CallTypeArgumentable(
    ) {
        super(
        );
        this.typearguments = new ArrayList<>();
    }

    public generics_CallTypeArgumentable(
        ArrayList<TypeArgument> typearguments    ) {
        this.typearguments = typearguments;
    }


    public List<TypeArgument> getTypearguments() {
        return typearguments;
    }

    public void addTypeargument(Typeargument typeargument) {
        this.typearguments.add(typeargument);
    }

}