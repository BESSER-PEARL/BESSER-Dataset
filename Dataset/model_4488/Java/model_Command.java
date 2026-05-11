





import java.util.List;
import java.util.ArrayList;

public class model_Command extends NamedElement {

    private String message;





    private model_Block model_block;




    private model_OzobotProgram model_ozobotprogram;




    private model_OzobotProgram model_ozobotprogram;


    public model_Command(
        String message    ) {
        super(
        );
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public model_Block getModel_block() {
        return model_block;
    }

    public void setModel_block(model_Block model_block) {
        this.model_block = model_block;
    }
    public model_OzobotProgram getModel_ozobotprogram() {
        return model_ozobotprogram;
    }

    public void setModel_ozobotprogram(model_OzobotProgram model_ozobotprogram) {
        this.model_ozobotprogram = model_ozobotprogram;
    }
    public model_OzobotProgram getModel_ozobotprogram() {
        return model_ozobotprogram;
    }

    public void setModel_ozobotprogram(model_OzobotProgram model_ozobotprogram) {
        this.model_ozobotprogram = model_ozobotprogram;
    }

}