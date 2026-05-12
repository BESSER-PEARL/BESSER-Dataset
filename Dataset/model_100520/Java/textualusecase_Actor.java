





import java.util.List;
import java.util.ArrayList;

public class textualusecase_Actor extends Agent {






    private List<textualusecase_UseCase> textualusecase_usecases;




    private textualusecase_UseCase textualusecase_usecase;




    private textualusecase_UseCaseModel textualusecase_usecasemodel;




    private textualusecase_UseCaseModel textualusecase_usecasemodel;


    public textualusecase_Actor(
    ) {
        super(
        );
        this.textualusecase_usecases = new ArrayList<>();
    }

    public textualusecase_Actor(
        ArrayList<textualusecase_UseCase> textualusecase_usecases    ) {
        this.textualusecase_usecases = textualusecase_usecases;
    }


    public List<textualusecase_UseCase> getTextualusecase_usecases() {
        return textualusecase_usecases;
    }

    public void addTextualusecase_usecase(Textualusecase_usecase textualusecase_usecase) {
        this.textualusecase_usecases.add(textualusecase_usecase);
    }
    public textualusecase_UseCase getTextualusecase_usecase() {
        return textualusecase_usecase;
    }

    public void setTextualusecase_usecase(textualusecase_UseCase textualusecase_usecase) {
        this.textualusecase_usecase = textualusecase_usecase;
    }
    public textualusecase_UseCaseModel getTextualusecase_usecasemodel() {
        return textualusecase_usecasemodel;
    }

    public void setTextualusecase_usecasemodel(textualusecase_UseCaseModel textualusecase_usecasemodel) {
        this.textualusecase_usecasemodel = textualusecase_usecasemodel;
    }
    public textualusecase_UseCaseModel getTextualusecase_usecasemodel() {
        return textualusecase_usecasemodel;
    }

    public void setTextualusecase_usecasemodel(textualusecase_UseCaseModel textualusecase_usecasemodel) {
        this.textualusecase_usecasemodel = textualusecase_usecasemodel;
    }

}