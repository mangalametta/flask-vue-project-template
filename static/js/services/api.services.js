async function getInfoFromBackend(text) {
    const reqData = { text }

    const response = await axios({
        method: "post",
        url: '/get-info-from-backend',
        data: reqData,
        headers: { 'Content-Type': 'application/json' }
    })

    if (response.status !== 200) return

    const resData = response.data
    if (!resData) return

    console.log(resData.message)
    return resData.data
}