





import java.util.List;
import java.util.ArrayList;

public class textualusecase_Condition  {

    private String expression;





    private textualusecase_UseCase textualusecase_usecase;




    private textualusecase_AlternativeFlow textualusecase_alternativeflow;




    private textualusecase_UseCase textualusecase_usecase;


    public textualusecase_Condition(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public textualusecase_UseCase getTextualusecase_usecase() {
        return textualusecase_usecase;
    }

    public void setTextualusecase_usecase(textualusecase_UseCase textualusecase_usecase) {
        this.textualusecase_usecase = textualusecase_usecase;
    }
    public textualusecase_AlternativeFlow getTextualusecase_alternativeflow() {
        return textualusecase_alternativeflow;
    }

    public void setTextualusecase_alternativeflow(textualusecase_AlternativeFlow textualusecase_alternativeflow) {
        this.textualusecase_alternativeflow = textualusecase_alternativeflow;
    }
    public textualusecase_UseCase getTextualusecase_usecase() {
        return textualusecase_usecase;
    }

    public void setTextualusecase_usecase(textualusecase_UseCase textualusecase_usecase) {
        this.textualusecase_usecase = textualusecase_usecase;
    }

}