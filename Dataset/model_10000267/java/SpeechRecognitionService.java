





import java.util.List;
import java.util.ArrayList;

public class SpeechRecognitionService  {

    private String speechRecognition;
    private boolean grabando;
    private String _attr;





    private Mensaje_Interface mensaje_interface;




    private ChatService chatservice;


    public SpeechRecognitionService(
        String speechRecognition,        boolean grabando,        String _attr    ) {
        this.speechRecognition = speechRecognition;
        this.grabando = grabando;
        this._attr = _attr;
    }


    public String getSpeechrecognition() {
        return speechRecognition;
    }

    public void setSpeechrecognition(String speechRecognition) {
        this.speechRecognition = speechRecognition;
    }
    public boolean getGrabando() {
        return grabando;
    }

    public void setGrabando(boolean grabando) {
        this.grabando = grabando;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }

    public Mensaje_Interface getMensaje_interface() {
        return mensaje_interface;
    }

    public void setMensaje_interface(Mensaje_Interface mensaje_interface) {
        this.mensaje_interface = mensaje_interface;
    }
    public ChatService getChatservice() {
        return chatservice;
    }

    public void setChatservice(ChatService chatservice) {
        this.chatservice = chatservice;
    }

}