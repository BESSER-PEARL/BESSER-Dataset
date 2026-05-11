





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_EmailMessage  {

    private String subject;
    private String sendAsHtml;
    private String smtpHost;
    private String id;
    private String smtpPort;
    private String timestamp;
    private String content;
    private String sourceId;



    public org_aries_common_EmailMessage(
        String subject,        String sendAsHtml,        String smtpHost,        String id,        String smtpPort,        String timestamp,        String content,        String sourceId    ) {
        this.subject = subject;
        this.sendAsHtml = sendAsHtml;
        this.smtpHost = smtpHost;
        this.id = id;
        this.smtpPort = smtpPort;
        this.timestamp = timestamp;
        this.content = content;
        this.sourceId = sourceId;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getSendashtml() {
        return sendAsHtml;
    }

    public void setSendashtml(String sendAsHtml) {
        this.sendAsHtml = sendAsHtml;
    }
    public String getSmtphost() {
        return smtpHost;
    }

    public void setSmtphost(String smtpHost) {
        this.smtpHost = smtpHost;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSmtpport() {
        return smtpPort;
    }

    public void setSmtpport(String smtpPort) {
        this.smtpPort = smtpPort;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getSourceid() {
        return sourceId;
    }

    public void setSourceid(String sourceId) {
        this.sourceId = sourceId;
    }


}