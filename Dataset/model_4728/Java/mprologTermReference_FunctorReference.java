





import java.util.List;
import java.util.ArrayList;

public class mprologTermReference_FunctorReference extends TermReference {






    private mprologTermReference_Term mprologtermreference_term;




    private mprologTermReference_Functor mprologtermreference_functor;


    public mprologTermReference_FunctorReference(
    ) {
        super(
        );
    }



    public mprologTermReference_Term getMprologtermreference_term() {
        return mprologtermreference_term;
    }

    public void setMprologtermreference_term(mprologTermReference_Term mprologtermreference_term) {
        this.mprologtermreference_term = mprologtermreference_term;
    }
    public mprologTermReference_Functor getMprologtermreference_functor() {
        return mprologtermreference_functor;
    }

    public void setMprologtermreference_functor(mprologTermReference_Functor mprologtermreference_functor) {
        this.mprologtermreference_functor = mprologtermreference_functor;
    }

}