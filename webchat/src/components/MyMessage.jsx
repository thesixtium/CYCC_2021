const MyMessage = ({message}) => {

    if(message?.attachments?.length > 0) {
        return (
            <img
                src={message.attachments[0].file}
                alt='messsage-attachment'
                className='message-image'
                style={{float: 'right'}}
            />
        )
    }
    return (
        <div className="message" style={{ float: 'right', marginRight: '18px', color: 'white', backgroundColor: '#1bb6bd' }}>
            {message.text}
        </div>
    )
}

export default MyMessage;