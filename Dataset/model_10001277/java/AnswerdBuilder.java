





import java.util.List;
import java.util.ArrayList;

public class AnswerdBuilder  {

    private None state;
    private String login;
    private String password;





    private ConcreteOtherAnswers concreteotheranswers;




    private ConcreteRightAnswers concreterightanswers;


    public AnswerdBuilder(
        None state,        String login,        String password    ) {
        this.state = state;
        this.login = login;
        this.password = password;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public ConcreteOtherAnswers getConcreteotheranswers() {
        return concreteotheranswers;
    }

    public void setConcreteotheranswers(ConcreteOtherAnswers concreteotheranswers) {
        this.concreteotheranswers = concreteotheranswers;
    }
    public ConcreteRightAnswers getConcreterightanswers() {
        return concreterightanswers;
    }

    public void setConcreterightanswers(ConcreteRightAnswers concreterightanswers) {
        this.concreterightanswers = concreterightanswers;
    }

}